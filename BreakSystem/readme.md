Chúng ta vào trang http://login.scoreboard.ns01.info/login.php và có giao diện:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/BreakSystem/login.PNG)

sau khi đăng ký chúng ta sẽ có giao diện:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/BreakSystem/home.PNG)

Không có gì trông có vẻ khai thác được ở đây, trừ việc username do ta kiểm soát được in ra trực tiếp, dẫn tới XSS và có tiềm năng SQLi.

Thử XSS không đưa tới kết quả khả quan, chúng ta nghĩ tới SQLi. Ở đây chúng ta inject từ register và là inject vào insert query. Thử đọc tên của database:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/BreakSystem/database.PNG)

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/BreakSystem/database2.PNG)

Giờ chúng ta có thể đọc tên bảng trong information_schema.tables. Với query "e',(select table_name from information_schema.tables limit 61,1),'1') -- -" chúng ta có tên bảng là "Fl4g". Và select * from Fl4g cho chúng ta flag:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/BreakSystem/flag.PNG)

flag: Flag{bl1nd_t1ming_h4rdc0r3_sl4shes}