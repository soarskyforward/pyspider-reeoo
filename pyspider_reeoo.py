#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-08-26 15:04:43
# Project: reeoo

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.reeoo.com', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('div[class="thumb"]').items():
            detail_url = each('a').attr.href
            self.crawl(detail_url, callback=self.detail_page,validate_cert=False)
        next = response.doc('.pagebar a:last').attr.href
        self.crawl(next,callback = self.index_page,validate_cert = False)
    @config(priority=2)
    def detail_page(self, response):
        tags = []
        for each in response.doc('.tags a').items():
            tags.append(each.text())
        return {
            "url": response.url,
            "title": response.doc('header > h1').text(),
            "description":response.doc('blockquote > p').text(),
            "image_url":response.doc('img[data-src]').attr('data-src'),
            "tags":tags,


        }
