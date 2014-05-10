#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class BanglaEncodingConverter:
	"""Converts Bengali Text between Encodings"""

	def replace(self, source, target, in_text):
		"""Returns a string encoded to target_encoding from source_encoding.
		Usage: replace(source_encoding, target_encoding, text)"""

		unicoded = (('অ', 'আ', 'ই', 'ঈ', 'উ', \
					'ঊ', 'ঋ‌', 'এ', 'ঐ', 'ও', \
					'ঔ', \

					'ক', 'খ', 'গ', 'ঘ', 'ঙ', \
					'চ', 'ছ', 'জ', 'ঝ', 'ঞ', \
					'ট', 'ঠ', 'ড', 'ঢ', 'ণ', \
					'ত', 'থ', 'দ', 'ধ', 'ন', \
					'প', 'ফ', 'ব', 'ভ', 'ম', \
					'য', 'র', 'ল', \
					'শ', 'স', 'ষ', 'হ', \
					'য়', 'ড়', 'ঢ়', \
					'ৎ', 'ং', 'ঃ', 'ঁ', \

					'া', 'ী', 'ু', 'ূ', 'ৃ', 'ৗ', \
					'০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'), \
					(r'(.)ি', r'(.)ে', r'(.)ৈ', r'(.)ো', r'(.)ৌ'),\
					(r'\1ি', r'\1ে', r'\1ৈ', r'\1ো', r'\1ৌ'))

		bijoy    = (('A', 'Av', 'B', 'C', 'D', \
					'E', 'F‌', 'G', 'H', 'I', \
					'J', \

					'K', 'L', 'M', 'N', 'O', \
					'P', 'Q', 'R', 'S', 'T', \
					'U', 'V', 'W', 'X', 'Y', \
					'Z', '_', '`', 'a', 'b', \
					'c', 'd', 'e', 'f', 'g', \
					'h', 'i', 'j', \
					'k', 'm', 'l', 'n', \
					'q', 'o', 'p', \
					'r', 's', 't', 'u', \

					'v', 'x', 'y', '~', '…', 'Š', \
					'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), \
					(r'w(.)', r'‡(.)', r'‰(.)', r'‡(.)v', r'‡(.)Š'), \
					(r'w\1', r'‡\1', r'‰\1', r'‡\1v', r'‡\1Š'))

		boishakhi = (('A', 'Aw', 'B', 'C', 'D', \
					'E', 'F‌', 'G', 'H', 'I', \
					'J', \

					'K', 'L', 'M', 'N', 'O', \
					'P', 'Q', 'R', 'S', 'T', \
					'U', 'V', 'W', 'X', 'Y', \
					'Z', 'a', 'b', 'c', 'd', \
					'e', 'f', 'g', 'h', 'i', \
					'j', 'k', 'l', \
					'm', 'o', 'n', 'p', \
					't', 'r', 's', \
					'u', 'v', ':', '^', \

					'w', 'y', '×', 'Ô', 'Ú', '#', \
					'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), \
					(r'x(.)', r'Ë(.)', r'Ð(.)', r'Ë(.)w', r'Ë(.)#'), \
					(r'x\1', r'Ë\1', r'Ð\1', r'Ë\1w', r'Ë\1#'))

		# need something better here
		if source == 'unicode': source_encoding = unicoded
		if source == 'bijoy': source_encoding = bijoy
		if source == 'boishakhi': source_encoding = boishakhi
		if target == 'unicode': target_encoding = unicoded
		if target == 'bijoy': target_encoding = bijoy
		if target == 'boishakhi': target_encoding = boishakhi

		for count in range(0, unicoded[0].__len__()):
			in_text = in_text.replace(source_encoding[0][count], target_encoding[0][count])

		for count in range(0, unicoded[1].__len__()):
			in_text = re.sub(source_encoding[1][count], target_encoding[2][count], in_text)

		return in_text