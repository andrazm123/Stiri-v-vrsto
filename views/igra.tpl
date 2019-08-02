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
  <table cellpadding="0" cellspacing="0" width="40%" class="plosca">
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

<div align="center" class="oznake">
    <table width="40%"><tr> 
      <td class="legenda" width="10%">
        <img src="/static/Igr.png" width="100%"  id="slika1"/>
      </td>
      <td width="23,3%">
        <p id="naslov1">YOU</p>
      </td>
      <td width="33,3%">123</td>
      <td width="23,3%"> 
          <h1 id="naslov2">COM</h1>
      </td>
      <td class="legenda" width="10%">
        <img src="/static/Rac.png" width="100%"  id="slika2"/>
      </td>
    </tr></table>
  </div>