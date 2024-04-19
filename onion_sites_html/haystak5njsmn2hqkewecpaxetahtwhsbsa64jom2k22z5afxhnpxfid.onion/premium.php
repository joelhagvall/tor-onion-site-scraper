<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>haystak: the darknet search engine</title>

    <!-- Bootstrap -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
      <style>
.result {
    padding-bottom: 2em;
}
</style>
  </head>
  <body>
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#"><i>haystak</i></a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li><a href="/">Search</a></li>
        <li><a href="/about.php">About</a></li>
        <li><a href="/premium.php">Go Premium</a></li>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
      <div class="container">
      <h1>Get Premium Services</h1>
<p>Our premium services offer considerably more than our free service:</p>

<table class="table">
    <thead>
        <th>What</th>
        <th>Free</th>
        <th>Premium</th>
    </thead>
    <tbody>
        <tr>
            <td>Text-based search of most of the darknet.</td>
            <td><span class="glyphicon glyphicon-ok"></span></td>
            <td><span class="glyphicon glyphicon-ok"></span></td>
        </tr>
        <tr>
            <td>Search of historical onions that have long since gone.</td>
            <td></td>
            <td><span class="glyphicon glyphicon-ok"></span></td>
        </tr>
        <tr>
            <td>Search using regular expressions</td>
            <td></td>
            <td><span class="glyphicon glyphicon-ok"></span></td>
        </tr>
        <tr>
            <td>Use our machine learning engine to find content of interest.</td>
            <td></td>
            <td><span class="glyphicon glyphicon-ok"></span></td>
        </tr>
        <tr>
            <td>Access to our dataset of bitcoins, e-mail addresses, visa card numbers, etc.</td>
            <td></td>
            <td><span class="glyphicon glyphicon-ok"></span></td>
        </tr>
        <tr>
            <td>Receive e-mail alerts when new content appears matching a term.</td>
            <td></td>
            <td><span class="glyphicon glyphicon-ok"></span></td>
        </tr>
        <tr>
            <td>Access to our API for querying our database automatically</td>
            <td></td>
            <td><span class="glyphicon glyphicon-ok"></span></td>
        </tr>
    </tbody>

</table>
<h2>Order</h2>
<p>Let us know what you're interested in and how to contact you if you want to discuss access to our premium services. We are a registered company.</p>
<form class="form" method="post" action="/report.php">
    <div class="form-group">
        <label for="name">Your name</label>
        <input type="text" class="form-control" name="name"/>
    </div>
    <div class="form-group">
        <label for="email">Your email</label>
        <input type="text" class="form-control" name="email"/>
    </div>
    <div class="form-group">
        <label for="company">Company</label>
        <input type="text" class="form-control" name="company"/>
    </div>
    <div class="form-group">
        <label for="name">How can we help you?</label>
        <textarea cols="80" rows="10" class="form-control" name="text"></textarea>
    </div>
    <input type="submit" class="btn btn-primary" value="Send"/>
</form>


      </div>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  </body>
</html>
