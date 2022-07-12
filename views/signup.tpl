<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<title>The Forum</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
	<style>
	:root {
		--main: #3C8A99;
		--contrast: #843DA8;
		--althighlight: #B8523D;
		--highlight: #6CC540;
	}

	.topnav {
	  overflow: hidden;
	  background-color: var(--main);
	}

	.topnav a {
	  float: right;
	  text-align: center;
	  padding: 14px 16px;
	  text-decoration: none;
	  font-size: 17px;
	}

	.topnav a:hover {
	  background-color: var(--highlight);
	  color: black;
	}

	.topnav a.active {
	  background-color: var(--contrast);
	  color: white;
	}
	</style>
</head>
<body>
	<div class="topnav">
		<a href="/signup" class="active">Registration</a>
		<a href="/login">Login</a>
		<a>User Account</a>
		<a>Saved Threads</a>
		<a href="/">Thread List</a>
	</div>
	<form action="/signup" method="post">
		username: <input name="username" type="text" />
		first name: <input name="first name" type="text" />
		last name: <input name="last name" type="text" />
		email address: <input name="email address" type="text" />
		password: <input name="password" type="password" />
		confirm password: <input name="confirm password" type="password" />
		<input value="Signup" type="submit" />
	</form>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy" crossorigin="anonymous"></script>
</body>
</html>