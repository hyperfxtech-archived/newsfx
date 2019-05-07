import unittest
from newsfx import NewsFX


class TestSum(unittest.TestCase):
    def test_tienphong(self):
        url = 'https://www.tienphong.vn/xa-hoi/chien-thang-dien-bien-phu-va-bai-hoc-the-tran-long-dan-1412151.tpo'
        run = NewsFX(url)
        run.parser()
        self.assertEqual(
            run.get_title, "Chiến thắng Điện Biên Phủ và bài học 'Thế trận lòng dân'", 'Should title')


if __name__ == '__main__':
    unittest.main()
