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