Truy cập vào trang http://megaupload.scoreboard.ns01.info/ chúng ta sẽ thấy 1 trang upload ảnh:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Megaupload/home.PNG)

Ý tưởng ở đây là chúng ta sẽ tìm cách upshell lên server. Thử test 1 lúc với chức năng upload của server thì thấy server sẽ chỉ nhận ảnh là jpg, đuôi file trong phần tên phải là jpg hoặc jpeg, mime-type là jpg hoặc jpeg. 

Chúng ta sẽ thêm 1 đoạn shell vào cuối 1 bức ảnh jpg (<?php system($_GET['c']); ?>), sau đó upload lên server:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Megaupload/upload.PNG)

Upshell thành công, giờ chúng ta cần biết shell ở đâu và làm sao để sử dụng. Ở đây đọc source ngay sau upload chúng ta sẽ thấy đường dẫn tới ảnh của chúng ta (img src="/heros/k4yG47l.jpg") và url có đoạn ?page=view cho thấy server dùng include dẫn tới LFI. việc còn lại chỉ là include shell và chạy lệnh.

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Megaupload/ls.PNG)

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Megaupload/flag.PNG)

flag: Flag{F1le_Upload_LF1}