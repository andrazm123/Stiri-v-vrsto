% rebase('views/base.tpl')
% import model


<div class="zgoraj">
  % if poteza == model.IG or poteza == model.RAC:
    <form action="/nova_igra/" method="post">
      <button class="gumb" type="submit">New game</button>
    </form>
  % else:
  <table class="gumbi">
    <tr>
      % for i in range(model.STOLPCI):
        <td>
          <form action="/ugibaj/{{i}}" method="post">
            <button class="gumb" type="submit">{{i + 1}}</button>
          </form>
        </td>
      % end
    </tr>
  </table>
  % end
</div>


<div>
  <table class="plosca">
    % for vrstica in range(model.VRSTICE):
      <tr valign="middel">
        % for stolpec in range(model.STOLPCI):
        <td>
          % if igra.tabela[vrstica][stolpec] == 0:
            <img src="/static/Be.jpg" width="100%"  /> 
          % elif igra.tabela[vrstica][stolpec] == -1:
            <img src="/static/Ru.jpg" width="100%"  />
          % else:
            <img src="/static/Rd.jpg" width="100%"  />
          % end
        </td>
        % end
      </tr>
    % end
  </table>
</div>

<div>
  <table class="reset">
    <tr>
      % if poteza == model.IG:
        <td id="zmagal"><h1 class="opis">You won!</h1></td>
      % elif poteza == model.RAC:
        <td id="izgubil"><h1 class="opis">You lost!</h1></td>
      % else:
        <td>
          <form action="/nova_igra/" method="post">
            <button class="gumb" type="submit">Reset</button>
          </form>
        </td>
      % end
    </tr>
  </table>
</div>

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


