from newsfx import NewsFX 

run = NewsFX('https://tuoitre.vn/chap-dien-chay-o-truong-mam-non-nguoi-dan-bac-thang-giai-cuu-hoc-sinh-20190513160005089.htm')
run.parser()
print(run.get_content) 

# with open ('test.txt','r') as f:
#     contend = f.read()

# from bs4 import BeautifulSoup as bs4

# suop = bs4(contend, 'lxml')

# xem = suop.findAll(attrs='p')
# print (suop.text)