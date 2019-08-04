% rebase('views/base.tpl')
% import model


<div align="center">
  % if poteza == model.IG or poteza == model.RAC:
    <form action="/nova_igra/" method="post">
      <button type="submit">Nova igra</button>
    </form>
  % else:
    <form action="/igra/" method="post">
      <input type="text" name="poskus">
      <input type="submit" value="Ugibaj">
    </form>
  % end
</div>


<div align="center">
  <table cellpadding="0" cellspacing="0" class="plosca">
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

<div id="s1">
    <img src="/static/Igr.png" class="slika"/>
</div>
<div id="s2">
    <h1>You</h1>
</div>
<div id="s3">
    <h1>Com</h1>
</div>
<div id="s4">
    <img src="/static/Rac.png" class="slika"/>
</div>
