% import model

<!DOCTYPE html>
<html lang="en">
  

  <head>
    <title>Vislice</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Andraž Maier">
  </head>


  <style>
    body{
      width: 40%;
      margin: auto;
      background-image: url("/static/Ozadje.jpg");
    }
    .zgoraj{
      margin-top: 4vw;
    }
    .gumbi{
      border-spacing: 0;
      width: 100%;
    }
    .gumbi td{
      line-height: 0;
      padding: 0;
    }
    .gumb{
      width: 100%;
      height: 2vw;
      font-size: 1vw;
      border: 0;
      background: #24305e;
      font-family: Arial, Helvetica, sans-serif;
      font-weight: bold;
      text-transform: uppercase;
      color: #c1d9e6;
    }
    .gumb:hover{
      background: #f76c6c;
      color: #24305e;
    }
    .plosca{
      border-spacing: 0;
    }
    .plosca td{
      line-height: 0;
      padding: 0;
    }
    .reset{
      border-spacing: 0;
      width: 100%;
    }
    .reset td{
      line-height: 0;
      padding: 0;
    }
    #zmagal{
      height: 2vw;
      font-size: 1vw;
      background: #f76c6c;
      text-align: center;
    }
    #izgubil{
      height: 2vw;
      font-size: 1vw;
      background: #f8e9a1;
      text-align: center;
    }
    .opis{
      font-family: Arial, Helvetica, sans-serif;
      font-weight: bold;
      text-transform: uppercase;
      color: #24305e;
      font-size: 1vw;
    }
    #s1{
      float: left;
      width: 15%;
    }
    #s2{
      float: left;
      width: 60%;
    }
    #s3{
      float: right;
      width: 10%;
    }
    #s4{
      float: right;
      width: 15%;
    }
    .slika{
      width: 80%;
    }
    .ime{
      font-family: Arial, Helvetica, sans-serif;
      font-size: 1.3vw;
      color: #24305e;
      font-weight: bold;
      text-transform: uppercase;
      margin-top: 2vw;
    }
    .naslov{
      font-family: Arial, Helvetica, sans-serif;
      font-size: 3vw;
      color: #24305e;
      font-weight: bold;
      text-transform: uppercase;
      margin-top:  15vw;
      margin-bottom: 5vw;
      text-align: center;
    }
    .gumb_nas{
      width: 100%;
      height: 3vw;
      font-size: 2vw;
      border: 0;
      background: #24305e;
      font-family: Arial, Helvetica, sans-serif;
      font-weight: bold;
      text-transform: uppercase;
      color: #c1d9e6;
    }
    .gumb_nas:hover{
      background: #f76c6c;
      color: #24305e;
    }

  </style>

  <body >
    {{!base}}
  </body>

</html>