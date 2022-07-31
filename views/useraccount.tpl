<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<title>The Forum - User Account</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
	<link href="/static/main.css" rel="stylesheet" type="text/css">
</head>
<body>
	<div id="logo"> 
		<a href="/">
			<img src="/static/logo.png" width="35%" alt="Forum Logo Link to Homepage">
		</a>
	</div> 
	<div class="topnav">
		<a href="/logout">Sign Out</a>
		<a href="/useraccount" class="active">User Account</a>
		<a href="/saved">Saved Threads</a>
		<a href="/">Thread List</a>
	</div>
	<div style="margin-top:80px;">
		%if Username_Taken:
		<div style="background-color: #cfc ; padding: 10px; border: 1px Solid Green;" class="text-center mt-5" style="max-width:300px;margin:auto;">
			<h2 style="color:rgb(132,61,168)">Username Taken. Try Another.</h2>
		</div>
		%elif Email_Taken:
		<div style="background-color: #cfc ; padding: 10px; border: 1px Solid Green;" class="text-center mt-5" style="max-width:300px;margin:auto;">
			<h2 style="color:rgb(132,61,168)">Email Taken. Try Another.</h2>
		</div>
		%elif Not_Same_Password:
		<div style="background-color: #cfc ; padding: 10px; border: 1px Solid Green;" class="text-center mt-5" style="max-width:300px;margin:auto;">
			<h2 style="color:rgb(132,61,168)">Password Not the Same.</h2>
		</div>
		%elif Changes_Success:
		<div style="background-color: #cfc ; padding: 10px; border: 1px Solid Green;" class="text-center mt-5" style="max-width:300px;margin:auto;">
			<h2 style="color:rgb(132,61,168)">Changes Success.</h2>
		</div>
		%end

		<div class="text-center mt-5">
			<form action="/useraccount" method="post" style="max-width:300px;margin:auto;">
				<h1 class="h3 mb-3 font-weight-normal" style="color:rgb(132,61,168)">Change Your Details</h1>
				<div>
					<label class="form-label" for="username" style="color:rgb(132,61,168)">Username</label>
					<input name="username" type="text" id="username" class="form-control" required autofocus value="{{user[0][0]}}">
				</div>
				<div>
					<label class="form-label" for="first-name" style="color:rgb(132,61,168)">First Name</label>
					<input name="first-name" type="text" id="first-name" class="form-control" required value="{{user[0][1]}}">
				</div>
				<div>
					<label class="form-label" for="last-name" style="color:rgb(132,61,168)">Last Name</label>
					<input name="last-name" type="text" id="last-name" class="form-control" required value="{{user[0][2]}}">
				</div>
				<div>
					<label class="form-label" for="email-address" style="color:rgb(132,61,168)">Email Address</label>
					<input name="email-address" type="email" id="email-address" class="form-control" required value="{{user[0][3]}}">
				</div>
				<div>
					<label class="form-label" for="password" style="color:rgb(132,61,168)">Password</label>
					<input name="password" type="password" id="password" class="form-control" required value="{{stored_info[0]}}">
				</div>
				<div>
					<label class="form-label" for="confirm-password" style="color:rgb(132,61,168)">Confirm Password</label>
					<input name="confirm-password" type="password" id="confirm-password" class="form-control" required value="{{stored_info[0]}}">
				</div>
				<div class="mt-3">
					<button class="btn btn-primary btn-success" style="color:var(--contrast)">Change Info</button>
				</div>
			</form>
		</div>
	</div>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy" crossorigin="anonymous"></script>
</body>
</html>