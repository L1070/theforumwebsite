<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<title>The Forum - Saved Threads</title>
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
		<a href="/login">Login</a>
	%elif user != "Guest":
		<a href="/logout">Sign Out</a>
		<a href="/useraccount">User Account</a>
		<a href="/saved" class="active">Saved Threads</a>
	%end
		<a href="/">Thread List</a>
	</div>
	<div style="margin-top:80px;">
		<div>
			<h1>
				Saved Thread List
			</h1>
		</div>
		<div>
			%if user == "Guest":
				<p>Guest</p>
			%else:
				%if user[0][5] == 1:
					<p>Admin {{user[0][1]}}</p>
				%else:
					<p>{{user[0][0]}}</p>
				%end
			%end
		</div>
		<div>
			%for entry in Saved_Threads:
				<div class="threadbox">
					<div class="row">
						<div class="column left">
							<h2>{{entry[0]}}</h2>
						</div>
						<div class="column middle">
							<a href="/threadpage/{{entry[0]}}"><h1>{{entry[1]}}</h1></a>
							<h3>{{entry[2]}} - {{entry[3]}}</h3>
						</div>
						<div class="column right" style="margin-top:2%">
							%if user != "Guest":
								<button>UP</button>
								<h5>{{entry[4]}}</h5>
								<button>DOWN</button>
							%else:
								<a  href="/login"><button>UP</button></a>
								<h5>{{entry[4]}}</h5>
								<a  href="/login"><button>DOWN</button></a>
							%end
						</div>
					</div>
					<div class="row" style="margin-top:3%;">
					%if user != "Guest":
						%if user[0][5] == 1:
							<div class="column littleleft">
								<button>PIN</button>
							</div>
							<div class="column littlemiddleadmin">
								<button>SAVE</button>
							</div>
						%else:
							<div class="column littlemiddle">
								<button>SAVE</button>
							</div>
						%end
						%if user[0][0] == entry[2]:
							<div class="column littleright">
								<button>DELETE</button>
							</div>
						%end
					%else:
						<div class="column littlemiddle">
							<a  href="/login"><button>SAVE</button></a>
						</div>
					%end
					</div>
				</div>
			%end
		</div>
	</div>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy" crossorigin="anonymous"></script>
</body>
</html>