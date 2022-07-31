<!DOCTYPE html>
<html lang="en">
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
			<img src="/static/logo.png" width="35%" alt="Forum Logo Link to Homepage">
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
		<div style="margin-left:20px;">
			<h1>
				Saved Thread List
			</h1>
		</div>
		<div>
			%if user == "Guest":
				<p style="margin-left:30px;">Guest</p>
			%else:
				%if user[0][5] == 1:
					<p style="margin-left:30px;">Admin {{user[0][1]}}</p>
				%else:
					<p style="margin-left:30px;">{{user[0][0]}}</p>
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
							<h2>{{entry[2]}} - {{entry[3]}}</h2>
						</div>
						<div class="column right" style="margin-top:2%">
							%if user != "Guest":
								<form action="/{{entry[0]}}/up/saved/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">UP</button></form>
								<h3>{{entry[4]}}</h3>
								<form action="/{{entry[0]}}/down/saved/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">DOWN</button></form>
							%else:
								<form action="/login"><button type="submit" value="To Login Page">UP</button></form>
								<h3>{{entry[4]}}</h3>
								<form action="/login"><button type="submit" value="To Login Page">DOWN</button></form>
							%end
						</div>
					</div>
					<div class="row" style="margin-top:3%;">
						%if user != "Guest":
							%if user[0][5] == 1:
								<div class="column littleleft">
									<form action="/pinthread/saved/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">PIN</button></form>
								</div>
								<div class="column littleright">
									<form action="/deletethread/saved/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">DELETE</button></form>
								</div>
							%else:
								%if user[0][6] == entry[5]:
									<div class="column littlerightcomment">
										<form action="/deletethread/saved/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">DELETE</button></form>
									</div>
								%end
							%end
						%end
					</div>
				</div>
			%end
		</div>
	</div>
	%if count > 20:
	<div>
		<div class="prevnextbox">
			<div class="row">
				%if pagenumber != 0:
					<div class="bottomcolumn bottomleft">
						<a  href="/saved/{{pagenumber-1}}"><button>PREV</button></a>
					</div>
				%end
				%if (count-offset_num) > 20:
					<div class="bottomcolumn bottomright">
						<a  href="/saved/{{pagenumber+1}}"><button>NEXT</button></a>
					</div>
				%end
			</div>
		</div>
	</div>
	%end
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy" crossorigin="anonymous"></script>
</body>
</html>