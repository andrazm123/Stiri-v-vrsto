% rebase('views/base.tpl')
% import model
<h1>Vislice</h1>

<table>
    <tr>
      <td><h3>{{ id_igre }}</h3></td>
    </tr>
    <tr>
      <td><h3>{{ igra.tabela }}</h3></td>
    </tr>
  
    % if poteza == model.IG or poteza == model.RAC:
    <form action="/nova_igra/" method="post">
      <button type="submit">Nova igra</button>
    </form>
  
    % else:
    <tr>
        <td bgcolor="blue">
          <form action="/igra/" method="post">
            <input type="text" name="poskus">
            <input type="submit" value="Ugibaj">
          </form>
        </td>
    </tr>
    % end
</table>


<div align="center">
  <table cellpadding="0" cellspacing="0" width="60%" border-spacing="0">
    % for vrstica in range(model.VRSTICE):
      <tr>
        % for stolpec in range(model.STOLPCI):
        <td>
          % if igra.tabela[vrstica][stolpec] == 0:
            <img src="/static/Bel.jpg" width="100%"  /> 
          % elif igra.tabela[vrstica][stolpec] == -1:
            <img src="/static/Rumen.jpg" width="100%"  />
          % else:
            <img src="/static/Rdec.jpg" width="100%"  />
          % end
        </td>
        % end
      </tr>
    % end     
  </table>
</div>