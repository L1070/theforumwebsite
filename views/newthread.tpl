<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<title>The Forum - New Thread</title>
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
		<a href="/useraccount">User Account</a>
		<a href="/saved">Saved Threads</a>
		<a href="/">Thread List</a>
	</div>
	<div style="margin-top:80px;">
		<div class="text-center mt-5">
			<form action="/newthread/page/{{pagenumber}}" method="post" style="max-width:800px;margin:auto;">
				<h1 class="h3 mb-3 font-weight-normal" style="color:rgb(132,61,168)">New Thread</h1>
				<div>
					<label class="form-label" for="title" style="color:rgb(132,61,168)">Title</label>
					<input name="title" type="text" id="username" class="form-control" required autofocus>
				</div>
				<div>
					<label class="form-label" for="content" style="color:rgb(132,61,168)">Content</label>
					<textarea name="content" type="text" id="content" class="form-control" required autofocus></textarea>
				</div>
				<div class="mt-3">
					<button class="btn btn-primary btn-success" style="color:var(--contrast)">Create Post</button>
				</div>
			</form>
		</div>
	</div>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy" crossorigin="anonymous"></script>
</body>
</html>