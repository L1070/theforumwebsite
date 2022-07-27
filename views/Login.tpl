<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<title>The Forum - Login</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
	<link href="/static/main.css" rel="stylesheet" type="text/css">
</head>
<body>
	<div id="logo"> 
		<a href="/">
			<img src="/static/logo.png" width="30%">
		</a>
	</div> 
	<div class="topnav">
	%if user == "Guest":
		<a href="/signup">Registration</a>
		<a href="/login" class="active">Login</a>
	%elif user != "Guest":
		<a href="/logout">Sign Out</a>
		<a href="/useraccount">User Account</a>
		<a href="/saved">Saved Threads</a>
	%end
		<a href="/">Thread List</a>
	</div>
	<div style="margin-top:80px;">
		%if LogInFailed:
		<div style="background-color: #cfc ; padding: 10px; border: 1px Solid Green;" class="text-center mt-5" style="max-width:300px;margin:auto;">
			<h2 style="color:rgb(132,61,168)">Incorrect Login. Try Again.</h2>
		</div>
		%elif Registration_Success:
		<div style="background-color: #cfc ; padding: 10px; border: 1px Solid Green;" class="text-center mt-5" style="max-width:300px;margin:auto;">
			<h2 style="color:rgb(132,61,168)">Registration Success!</h2>
		</div>
		%end

		<div class="text-center mt-5">
			<form action="/login" method="post" style="max-width:300px;margin:auto;">
				<h1 class="h3 mb-3 font-weight-normal" style="color:rgb(132,61,168)">Please Login</h1>
				<label class="form-label" for="username" style="color:rgb(132,61,168)">Username</label>
				<input name="username" type="text" id="username" class="form-control" required autofocus>
				<label class="form-label" for="password" style="color:rgb(132,61,168)">Password</label>
				<input name="password" type="password" id="password" class="form-control" required autofocus>
				<div>
					<label>
						<input type="checkbox" value="remember-me"> Remember Me
					</label>
				</div>
				<div class="mt-3">
					<button class="btn btn-primary btn-success" style="color:rgb(132,61,168)">Login!</button>
				</div>
			</form>
		</div>
	</div>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy" crossorigin="anonymous"></script>
</body>
</html>