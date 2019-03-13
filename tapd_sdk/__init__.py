#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
import json
import requests
from requests.auth import HTTPBasicAuth

# 请求类型对应url
request_type_url = {
    "stories": "https://api.tapd.cn/stories",  # 需求
    "tasks": "https://api.tapd.cn/tasks"       # 任务
}


def request_api_result(user, password, url, parms):
    req = requests.get(url, params=parms, auth=HTTPBasicAuth(user, password))
    data = json.loads(req.content.decode('utf8'))
    return data


class TAPD(object):

    """
    经跟客服确认，只有【数据查询接口特别说明】上的字段名才支持文档上的查询方法
    所以API只支持单个workspace_id和owner的查询
    Api doc: https://www.tapd.cn/help/view#1120003271001001250
    """

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def get_tapd_data(self, data_type, workspace_id, status=None,
                      owner=None, start_date=None, end_date=None):
        """
        状态为normal项目才能获取到工单信息，
        否则返回{'status': 403, 'data': '', 'info': 'no rights to access this project'}
        """
        if not isinstance(data_type, str):
            raise TypeError("request_type must be string.")
        if not isinstance(workspace_id, int):
            raise TypeError("workspace_id must be int.")

        parms = {"workspace_id": workspace_id}

        if status:
            if not isinstance(status, str):
                raise TypeError("status must be string.")
            parms["status"] = status

        if owner:
            if not isinstance(owner, str):
                raise TypeError("owner must be str.")
            parms["owner"] = owner

        if start_date and end_date:
            if not isinstance(start_date, date):
                raise TypeError("start_date must be date.")
            if not isinstance(end_date, date):
                raise TypeError("end_date must be date.")
            parms["created"] = str(start_date) + "~" + str(end_date)

        try:
            req_url = request_type_url[data_type]
        except KeyError:
            raise ValueError("request_type must be " + ' or '.join(request_type_url.keys()))
        data = request_api_result(self.user, self.password, req_url, parms)
        return data

    def get_projects_info(self, company_id, status=None):

        projects_url = "https://api.tapd.cn/workspaces/projects"
        parms = {"company_id": company_id}
        projects_info = request_api_result(user=self.user,
                                           password=self.password,
                                           url=projects_url,
                                           parms=parms)
        if status:
            projects_info = [project for project in projects_info["data"]
                             if project["Workspace"]["status"] == status]
        else:
            projects_info = projects_info["data"]
        return projects_info

    def get_workspace_users(self, workspace_id):
        url = "https://api.tapd.cn/workspaces/users?fields=user,email,role_id"
        parms = {"workspace_id": workspace_id}
        workspace_users = request_api_result(user=self.user,
                                             password=self.password,
                                             url=url,
                                             parms=parms)
        return workspace_users