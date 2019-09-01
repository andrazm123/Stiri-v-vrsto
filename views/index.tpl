% rebase('views/base.tpl')
% import model

<section>
  <div class="naslovnica">
    <h1 class="naslov">Four in a row</h1>
    <form action="/nova_igra/{{model.IG}}/{{model.TEZKO}}" method="post">
      <button class="gumb_nas" type="submit">Hard</button>
    </form>
    <form action="/nova_igra/{{model.IG}}/{{model.LAHKO}}" method="post">
      <button class="gumb_nas" type="submit">Easy</button>
    </form>
    <form action="/nova_igra/{{model.RAC}}/{{model.TEZKO}}" method="post">
      <button class="gumb_nas_r" type="submit">Hard</button>
    </form>
    <form action="/nova_igra/{{model.RAC}}/{{model.LAHKO}}" method="post">
      <button class="gumb_nas_r" type="submit">Easy</button>
    </form>
    <form action="/nova_igra/{{model.DVA_IGRALCA_1}}/{{model.TEZKO}}" method="post">
      <button class="gumb_nas" type="submit">Two players</button>
    </form>
  </div>
</section>

<section>
  <div id="s1">
      <img src="/static/Igr.png" class="slika"/>
  </div>
  <div id="s2">
      <h1 class="ime">You</h1>
  </div>
  <div id="s3">
      <h1 class="ime">Com</h1>
  </div>
  <div id="s4">
      <img src="/static/Rac.png" class="slika"/>
  </div>
</section>
