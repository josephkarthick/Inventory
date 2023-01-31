{% load static%}
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0">
<title> Tridots Inventory</title>
<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
<link rel="stylesheet" href="{% static 'css/animate.css' %}">
<link rel="stylesheet" href="{% static 'css/dataTables.bootstrap4.min.css' %}">
<link rel="stylesheet" href="{% static 'css/dataTables.bootstrap-datetimepicker.min.css' %}">
<link rel="stylesheet" href="{% static 'css/fontawesome.min.css' %}">
<link rel="stylesheet" href="{% static 'css/all.min.css' %}">
<link rel="stylesheet" href="{% static 'css/style.css'%}">
<link rel="stylesheet" href="{% static 'css/select2.min.css'%}">

</head>
<div class="header">
	<div class="header-left active">
	<a href="#" class="logo logo-normal">
		<img src="{%static 'img/logo.png' %}" alt="">
	</a>
	</div>
</div>

<div class="main-wrapper">
<div class="sidebar" id="sidebar">
<div class="sidebar-inner slimscroll">
<div id="sidebar-menu" class="sidebar-menu">
<ul>

<li class="">
<a href="{%url 'viewproduct'%}"><img src="{% static 'img/product.svg'%}" alt="img"><span> Product</span></a>
</li>

<li class="">
<a href="{%url 'viewlocation' %}"><img src="{% static 'img/location.svg'%}" alt="img"><span> Location</span></a>

</li>

<li class="">
<a href="{%url 'viewmovement'%}"><img src="{% static 'img/movement.svg' %}" alt="img"><span> Product Movement</span></a>

</li>

</ul>
</div>
</div>
</div>


</div>


<script src="https://dreamspos.dreamguystech.com/html/template/assets/js/jquery-3.6.0.min.js"></script>
<script src="https://dreamspos.dreamguystech.com/html/template/assets/js/feather.min.js"></script>
<script src="https://dreamspos.dreamguystech.com/html/template/assets/plugins/select2/js/select2.min.js"></script>
<script src="https://dreamspos.dreamguystech.com/html/template/assets/js/script.js"></script>