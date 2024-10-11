from django.utils.safestring import mark_safe	# django为了安全会默认拒绝渲染后端的html代码，所以我们需要mark_safe()给html代码标记为安全，才可以在前端渲染

class Pagination(object):
    """自定义分页组件"""

    def __init__(self, request, temp_name_param, queryset, search_data, time_data,
                 page_size=15, nex=5, prev=5, first_switch=True,
                 last_switch=True, a_next=True, a_prev=True):
        self.search_data = search_data
        self.time_data = time_data
        # 当前页码
        now_page = request.GET.get(temp_name_param, 1)

        # 是否是数字
        if now_page == 1:
            pass
        elif now_page.isdecimal():
            now_page = int(now_page)
        else:
            # 不是数据就默认为1
            now_page = 1

        # 当前页
        self.now_page = now_page
        # 每页显示数
        self.page_size = page_size
        # 数据总量
        self.total = queryset.count()
        # 切片开始位
        self.start = (now_page - 1) * page_size
        # 切片结束位
        self.end = now_page * page_size
        # 对ORM从数据库中拿到的数据进行切片，获得当前页面所对应的数据
        self.page_queryset = queryset[self.start:self.end]
        # 总页数
        self.page_num = int(self.total / self.page_size)
        if self.total == 0:
            self.page_num = 1
        elif self.total % self.page_size:
            self.page_num += 1

        # 显示当前页的前多少页
        self.nex = nex
        # 显示当前页的后多少页
        self.prev = prev

        # 组件调用
        self.first_switch = first_switch  # 是否显示 首页跳转 组件
        self.last_switch = last_switch  # 是否显示 尾页跳转 组件
        self.a_next = a_next  # 是否显示 上一页跳转 组件
        self.a_prev = a_prev  # 是否显示 下一页跳转 组件

    def page_first(self):
        """ 添加首页页码的html代码
        :return: （str）html代码
        """
        return f'<li class="page-item"><a class="page-link" href="?time={self.time_data}&search={self.search_data}&page=1">首页</a></li>'

    def page_last(self):
        """ 添加尾页页码的html代码
        :return: （str）html代码
        """
        return f'<li class="page-item"><a class="page-link"href="?time={self.time_data}&search={self.search_data}&page={self.page_num}">尾页</a></li>'

    def page_next(self):
        """ 添加下一页的html代码
        :return: （str）html代码
        """
        if self.now_page == self.page_num:
            html = f'<li class="disabled page-item"><a class="page-link"href="?time={self.time_data}&search={self.search_data}&page={self.page_num}" aria-label="Next"><span aria-hidden="true">»</span></a></li>'
        else:
            html = f'<li class="page-item"><a class="page-link"href="?time={self.time_data}&search={self.search_data}&page={self.now_page + 1}" aria-label="Next"><span aria-hidden="true">»</span></a></li>'
        return html

    def page_prev(self):
        if self.now_page == 1:
            html = f'<li class="disabled page-item"><a class="page-link"href="?time={self.time_data}&search={self.search_data}&page=1" aria-label="Previous"><span aria-hidden="true">«</span></a></li>'
        else:
            html = f'<li class="page-item"><a class="page-link"href="?time={self.time_data}&search={self.search_data}&page={self.now_page - 1}" aria-label="Previous"><span aria-hidden="true">«</span></a></li>'
        return html

    def basic(self):
        """ 生成基础的html代码
        :return: （str）html代码
        """
        nex_html = ""
        if self.now_page <= self.nex:
            nex_list = range(1, self.now_page)
        else:
            nex_list = range(self.now_page - self.nex, self.now_page)
        for page in nex_list:
            nex_html += f'<li class="page-item"><a class="page-link"href="?time={self.time_data}&search={self.search_data}&page={page}">{page}</a></li>'

        now_html = f'<li class="active page-item"><a class="page-link"href="?time={self.time_data}&search={self.search_data}&page={self.now_page}">{self.now_page}</a></li>'

        prev_html = ""
        if self.page_num - self.now_page <= self.prev:
            prev_list = range(self.now_page + 1, self.page_num + 1)
        else:
            prev_list = range(self.now_page + 1, self.now_page + self.prev + 1)
        for page in prev_list:
            prev_html += f'<li class="page-item"><a class="page-link"href="?time={self.time_data}&search={self.search_data}&page={page}">{page}</a></li>'

        return nex_html + now_html + prev_html

    def html(self):
        """ 生成全部的html
        :return: (str) html代码
        """
        html = ""
        if self.first_switch:
            html += self.page_first()
        if self.a_prev:
            html += self.page_prev()
        html += self.basic()
        if self.a_next:
            html += self.page_next()
        if self.last_switch:
            html += self.page_last()

        return mark_safe(html)
