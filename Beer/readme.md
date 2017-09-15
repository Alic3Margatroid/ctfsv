Chúng ta vào trang http://cannotbruteforce.scoreboard.ns01.info/ và có giao diện:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Beer/home.PNG)

Đọc source và vào index.txt chúng ta có source code:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Beer/source.PNG)

Chúng ta thử test đoạn code này:

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

và nhận thấy ở var_dump thứ 2 kết quả khá thú vị:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Beer/test.PNG)