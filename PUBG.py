# @Author  : ShiRui

import pygal
import requests
import jsonpath
import json


class PUBG(object):

	# 初始变量
	def __init__(self):

		self.data = []
		self.num = 0
		self.url = "http://pg.qq.com/zlkdatasys/data_zlk_zlzx.json"
		self.header = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0',
		}

	# 爬去数据
	def crwalData(self):

		num = 0
		response = requests.get(self.url, self.header)
		html = response.text

		unicodest = json.loads(html)
		# 优缺点
		ad2disad = jsonpath.jsonpath(unicodest, "$..yd_c6")

		# 性能
		performance = jsonpath.jsonpath(unicodest, "$..ldtw_f2")

		# 名字
		names = jsonpath.jsonpath(unicodest, "$..mc_94")

		for i in performance:
			if num < 7:
				self.num += 1
				self.data.append([int(i[0]['wl_45']), int(i[0]['sc_54']), int(i[0]['ss_d0']), int(i[0]['wdx_a7']), int(i[0]['zds_62'])])

		return names

	# 数据处理
	def analysis(self):

		try:
			names = self.crwalData()
			radar = pygal.Radar()
			radar.title = "步枪的性能"
			radar.x_labels = ['威力', '射程', '射速', '稳定性', '子弹数']
			for name, character in zip(names[1:8], self.data):
				radar.add(name, character)
			radar.render_to_file("weapon.svg")

		except Exception as e:

			print(e)

if __name__ == '__main__':

	pubg = PUBG()
	pubg.analysis()
	print("程序运行完成！")
