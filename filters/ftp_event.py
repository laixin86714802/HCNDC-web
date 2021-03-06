# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from server.decorators import make_decorator


class FtpEventFilter(object):
    @staticmethod
    @make_decorator
    def filter_get_ftp_event(result, total):
        """获取文件事件列表"""
        for item in result:
            if item['next_run_time']:
                item['next_run_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item['next_run_time']))
            else:
                item['next_run_time'] = ''
        return {'status': 200, 'msg': '成功', 'total': total, 'data': result}, 200

    @staticmethod
    @make_decorator
    def filter_get_ftp_event_detail(result):
        """获取文件事件详情"""
        return {'status': 200, 'msg': '成功', 'data': result}, 200

    @staticmethod
    @make_decorator
    def filter_update_ftp_event_detail(ftp_event_id):
        """修改文件事件详情"""
        return {'status': 200, 'msg': '成功', 'data': {'id': ftp_event_id}}, 200

    @staticmethod
    @make_decorator
    def filter_add_dispatch(ftp_event_id):
        """修改文件事件详情"""
        return {'status': 200, 'msg': '成功', 'data': {'id': ftp_event_id}}, 200

    @staticmethod
    @make_decorator
    def filter_test_data(status, msg):
        """测试FTP文件目录是否存在"""
        return {'status': status, 'msg': msg, 'data': {}}, 200

    @staticmethod
    @make_decorator
    def filter_action_ftp_event(ftp_event_id):
        """暂停/恢复调度事件"""
        return {'status': 200, 'msg': '成功', 'data': {'id': ftp_event_id}}, 200

    @staticmethod
    @make_decorator
    def filter_delete_ftp_event_detail(ftp_event_id):
        """删除调度详情"""
        return {'status': 200, 'msg': '成功', 'data': {'id': ftp_event_id}}, 200

    @staticmethod
    @make_decorator
    def filter_run_ftp_event(ftp_event_id):
        """立即执行调度任务"""
        return {'status': 200, 'msg': '成功', 'data': {'id': ftp_event_id}}, 200