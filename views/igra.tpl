% rebase('views/base.tpl')
% import model

<section>
  <div class="zgoraj">
    <table class="gumbi">
      % if igra.igralec == model.DVA_IGRALCA_1 or igra.igralec == model.DVA_IGRALCA_2:
        % if poteza == model.IG:
          <tr><td id="zmagal"><h1 class="opis">Player one won!</h1></td></tr>
        % elif poteza == model.RAC:
          <tr><td id="izgubil"><h1 class="opis">Player two won!</h1></td></tr>
        % elif poteza == model.REMI:
          <td class="remi">
            <h1>Draw!</h1>
          </td>
        % else:
          <tr>
            % if igra.igralec == model.DVA_IGRALCA_1:
              % for i in range(model.STOLPCI):
                <td>
                  <form action="/ugibaj/{{i}}" method="post">
                    <button class="gumb" type="submit">{{i + 1}}</button>
                  </form>
                </td>
              % end
            % else:
              % for i in range(model.STOLPCI):
                <td>
                  <form action="/ugibaj/{{i}}" method="post">
                    <button class="gumb1" type="submit">{{i + 1}}</button>
                  </form>
                </td>
              % end
            % end
          </tr>
        % end        
      % else:
        % if poteza == model.IG:
          <tr><td id="zmagal"><h1 class="opis">You won!</h1></td></tr>
        % elif poteza == model.RAC:
          <tr><td id="izgubil"><h1 class="opis">You lost!</h1></td></tr>
        % elif poteza == model.REMI:
          <td class="remi">
            <h1>Draw!</h1>
          </td>
        % else:
          <tr>
            % for i in range(model.STOLPCI):
              <td>
                <form action="/ugibaj/{{i}}" method="post">
                  <button class="gumb" type="submit">{{i + 1}}</button>
                </form>
              </td>
            % end
          </tr>
        % end
      % end
    </table>
  </div>


  <div>
    <table class="plosca">
      % for vrstica in range(model.VRSTICE):
        <tr valign="middel">
          % for stolpec in range(model.STOLPCI):
          <td>
            % if igra.tabela[vrstica][stolpec] == model.PRAZNO:
              <img src="/static/Be.jpg" width="100%"  /> 
            % elif igra.tabela[vrstica][stolpec] == model.RAC:
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
        % if poteza == model.IG or poteza == model.RAC or poteza == model.REMI:
          <td>
            <form action="/" method="post">
              <button class="gumb" type="submit">New game</button>
            </form>
          </td>
        % elif poteza == model.NAPAKA:
        <td class="napaka">         
          <h1>Incorrect move!!!</h1>
        </td>
        % else:
          <td>
            <form action="/" method="post">
              <button class="gumb" type="submit">Reset</button>
            </form>
          </td>
        % end
      </tr>
    </table>
  </div>
</section>

<section>
  <div id="s1">
    <img src="/static/Igr.png" class="slika"/>
  </div>
  <div id="s2">
    % if igra.igralec == model.DVA_IGRALCA_1 or igra.igralec == model.DVA_IGRALCA_2:
      <h1 class="ime">Player one</h1>
    % else:
      <h1 class="ime">You</h1>
    % end
  </div>
  <div id="s3">
    % if igra.igralec == model.DVA_IGRALCA_1 or igra.igralec == model.DVA_IGRALCA_2:
      <h1 class="ime">Player two</h1>
    % else:
      <h1 class="ime">Com</h1>
    % end
  </div>
  <div id="s4">
      <img src="/static/Rac.png" class="slika"/>
  </div>
</section>

