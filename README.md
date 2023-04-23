# Calcular DV de NUP

Fiz este código/página que calcula os 2 dígitos verificadores (DV) dos Números Únicos de Protocolo (NUP) da Administração Pública federal de acordo com as regras estabelecidas na [Portaria Interministerial No. 11](https://www.in.gov.br/web/dou/-/portaria-interministerial-n-11-de-25-de-novembro-de-2019-229645093), de 25 de novembro de 2019.

Ele está rodando no [PythonAnywhere](https://www.pythonanywhere.com/) para quaisquer NUP [aqui](https://mcpinto.pythonanywhere.com/teste) (ou estava rodando, agora já não sei). O código é em Python 3.10 e a integração com o HTML é feita usando Flask 2.1.

Eu tinha feito ele para rodar somente para os NUP da Universidade Federal da Integração Latino-Americana ([UNILA](https://portal.unila.edu.br/)), mas acabou ficando fácil generalizar, então está aí essa versão "expandida".


## Arquivos

### `processing.py`

É onde está o código propriamente dito (e a parte que deu menos trabalho).

É composto apenas por uma função `getDV()`, que faz os cálculos conforme a Portaria 11/2019 indica.

### `flask_app.py`

É a parte que recebe os parâmetros do formulário HTML, os repassa para `getDV()` e, depois, devolve o DV calculado para o HTML exibir.

Totalmente "inspirado" [daqui](https://blog.pythonanywhere.com/169/).


### `main_page.html`

É a página HTML com o formulário para entrada dos parâmetros do NUP integrado com código Python usando Flask para exibir eventuais erros e o DV calculado.

Totalmente "inspirado" [daqui](https://blog.pythonanywhere.com/121/).


## Atualizações, direitos *et al*

Se você quiser alterações, fique a vontade para solicitar (mas não espere que eu vá atender). Você também pode pegar os arquivos e ser feliz fazendo as adaptações que preferir.

Os códigos são **"*as is*"**, ou seja, não tem garantia nenhuma. Use por sua conta e risco. Não venha reclamar comigo muito menos me processar.

Este código tem a licença **[The Unlicense](https://unlicense.org/)**, ou seja, os arquivos são de domínio público. Use como quiser, referencie se quiser, avise-me que usou se quiser. Tenho mais o que fazer do que me preocupar com licenças de software.
