<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>The Forum - Signup</title>
    </head>
<body style="background-color:rgb(60, 138, 153);">

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
%end

<div class="text-center mt-5">
    <form action="/signup" method="post" style="max-width:300px;margin:auto;">
        <h1 class="h3 mb-3 font-weight-normal" style="color:rgb(132,61,168)">Signup</h1>
        <div>
            <label class="form-label" for="username" style="color:rgb(132,61,168)">Username</label>
            <input name="username" type="text" id="username" class="form-control" required autofocus>
        </div>
        <div>
            <label class="form-label" for="first-name" style="color:rgb(132,61,168)">First Name</label>
            <input name="first-name" type="text" id="first-name" class="form-control" required autofocus>
        </div>
        <div>
            <label class="form-label" for="last-name" style="color:rgb(132,61,168)">Last Name</label>
            <input name="last-name" type="text" id="last-name" class="form-control" required autofocus>
        </div>
        <div>
            <label class="form-label" for="email-address" style="color:rgb(132,61,168)">Email Address</label>
            <input name="email-address" type="email" id="email-address" class="form-control" required autofocus>
        </div>
        <div>
            <label class="form-label" for="password" style="color:rgb(132,61,168)">Password</label>
            <input name="password" type="password" id="password" class="form-control" required autofocus>
        </div>
        <div>
            <label class="form-label" for="confirm-password" style="color:rgb(132,61,168)">Confirm Password</label>
            <input name="confirm-password" type="password" id="confirm-password" class="form-control" required autofocus>
        </div>
        <div class="mt-3">
            <button class="btn btn-primary btn-success" style="color:rgb(132,61,168)">Signup!</button>
        </div>
    </form>
</div>

<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</body>
</html>
