Chúng ta vào trang http://cannotbruteforce.scoreboard.ns01.info/ và có giao diện:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Beer/home.PNG)

Đọc source và vào index.txt chúng ta có source code:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Beer/source.PNG)

Chúng ta thử test đoạn code này:
```php

$user_list = array(
	0 => array('username' => 'admin', 'password' => 'xxxxxxxxxxxxxxxxxxxx'),
	1 => array('username' => 'user1', 'password' => 'xxxxxxxxxxxxxxxxxxxxxxxxx'),
	2 => array('username' => 'user2', 'password' => 'xxxxxxxxxxxxxxxxxxxxxxxxx'),
	3 => array('username' => 'user3', 'password' => 'xxxxxxxxxxxxxxxxxxxxxxxxx'),
	4 => array('username' => 'user4', 'password' => 'xxxxxxxxxxxxxxxxxxxxxxxxx'),
	5 => array('username' => 'user5', 'password' => 'xxxxxxxxxxxxxxxxxxxxxxxxx'),
	6 => array('username' => 'user6', 'password' => 'xxxxxxxxxxxxxxxxxxxxxxxxx')
);

var_dump($user_list);

function add_prefix($username) {
	return "ANM_" . $username;
}

foreach ($user_list as & $user) {
	$user['username'] = add_prefix($user['username']);
}

var_dump($user_list);

```

và nhận thấy ở var_dump thứ 2 kết quả khá thú vị:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Beer/test.PNG)

Ở đây ta thấy user_list[6] lại là được trỏ bởi 1 con trỏ. Điều này xảy ra do khi iterate hết user_list, trang web đã quên không free user, nên con trỏ ở đây chính là của user. Vì vậy khi xử lý $_GET['user'], thực tế là user_list[6] bị điều khiển bởi người dùng. Chúng ta sẽ có ý tưởng sửa giá trị của user_list[6] thành giá trị ta mong muốn, sau đó truyền user_list[6](hay ở đây là user[6]) là giá trị user.

Ví dụ với đoạn code sau:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Beer/modifycode.PNG)

Chúng ta có thể sửa được giá trị name của user_list[6] về admin 1 cách dễ dàng:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Beer/modifyresult.PNG)

Và giờ chúng ta quay lại với bài ở đây, truyền thêm password là chúng ta đạt được mục đích:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Beer/flag.PNG)

flag: Flag{W3b_wr0oong_With_&_}