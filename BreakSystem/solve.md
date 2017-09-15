Chúng ta vào trang http://login.scoreboard.ns01.info/login.php và có giao diện:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/BreakSystem/login.PNG)

sau khi đăng ký chúng ta sẽ có giao diện:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/BreakSystem/home.PNG)

Không có gì trông có vẻ khai thác được ở đây, trừ việc username do ta kiểm soát được in ra trực tiếp, dẫn tới XSS và có tiềm năng SQLi.

Thử XSS không đưa tới kết quả khả quan, chúng ta nghĩ tới SQLi. Ở đây chúng ta inject từ 
