<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<title>The Forum</title>
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
		<a href="/saved">Saved Threads</a>
	%end
		<a href="/" class="active">Thread List</a>
	%if user != "Guest":
		<a href="/newthread/{{pagenumber}}">New Thread</a>
	%end
	</div>
	<div style="margin-top:80px;">
		<div style="margin-left:20px;">
			<h1>
				Thread List
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
			%for entry in PinnedThreads:
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
								<a href="/{{entry[0]}}/up/home/page/{{pagenumber}}"><button>UP</button></a>
								<h5>{{entry[4]}}</h5>
								<a href="/{{entry[0]}}/down/home/page/{{pagenumber}}"><button>DOWN</button></a>
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
									<form action="/pinthread/home/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">PIN</button></form>
								</div>
								<div class="column littlemiddleadmin">
									<form action="/savethread/home/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">SAVE</button></form>
								</div>
									<div class="column littleright">
										<form action="/deletethread/home/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">DELETE</button></form>
									</div>
							%else:
								<div class="column littlemiddle">
									<form action="/savethread/home/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">SAVE</button></form>
								</div>
								%if user[0][6] == entry[5]:
									<div class="column littleright">
										<form action="/deletethread/home/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">DELETE</button></form>
									</div>
								%end
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
		<div>
			%for entry in UnPinnedThreads:
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
								<a href="/{{entry[0]}}/up/home/page/{{pagenumber}}"><button>UP</button></a>
								<h5>{{entry[4]}}</h5>
								<a href="/{{entry[0]}}/down/home/page/{{pagenumber}}"><button>DOWN</button></a>
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
									<form action="/pinthread/home/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">PIN</button></form>
								</div>
								<div class="column littlemiddleadmin">
									<form action="/savethread/home/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">SAVE</button></form>
								</div>
									<div class="column littleright">
										<form action="/deletethread/home/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">DELETE</button></form>
									</div>
							%else:
								<div class="column littlemiddle">
									<form action="/savethread/home/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">SAVE</button></form>
								</div>
								%if user[0][6] == entry[5]:
									<div class="column littleright">
										<form action="/deletethread/home/page/{{pagenumber}}" method="post"><button type="submit" name="threadid" value="{{entry[0]}}">DELETE</button></form>
									</div>
								%end
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
	%if count > 20:
	<div>
		<div class="prevnextbox">
			<div class="row">
				%if pagenumber != 0:
					<div class="bottomcolumn bottomleft">
						<a  href="/page/{{pagenumber-1}}"><button>PREV</button></a>
					</div>
				%end
				%if (count-offset_num) > 20:
					<div class="bottomcolumn bottomright">
						<a  href="/page/{{pagenumber+1}}"><button>NEXT</button></a>
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
