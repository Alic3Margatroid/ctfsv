Chúng ta truy cập vào trang http://sqli.scoreboard.ns01.info/ sẽ thấy giao diện:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Sqlisqli/home.PNG)

Vào source: 

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Sqlisqli/source.PNG)

Đây là 1 sqli filter đơn giản để filter dấu ' và ở đây sử dụng hàm strpos. Tuy nhiên nếu dấu ' ở ngay đầu tiên thì strpos sẽ trả lại 0, tương đương với false trong mệnh đề điều kiện, dẫn tới việc bypass được filter.

Chúng ta sử dụng payload ?username=' or 1=1 limit 1 -- - &password=1 để thử và có ngay flag:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Sqlisqli/flag.PNG)

flag: Flag{SQL_Injection_Filter_Apostrophe}