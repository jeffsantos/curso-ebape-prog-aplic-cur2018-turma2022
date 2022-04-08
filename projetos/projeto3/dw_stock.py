# 1 - Import das bibliotecas necessárias

# 2 - Ler uma lista de ações como parâmetros passados para o programa pelo terminal


# 3 - Peça para o usuário informar uma data de inicio e uma data de fim para buscar os dados


# 4 - Loop principal: para cada código de ação informado:

    # 4.1 - Preparar a url do site Yahoo Finanças com os dados da ação

        # 'https://br.financas.yahoo.com/quote/VALE/history?period1=1577836800&period2=1609372800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'


    # 4.2 - Obter a página de resposta para a url preparada acima (dica: requests.get())


    # 4.3 - Scrap na página: 
    # No html da página de resultado (que vc leu acima), há uma table que exibe os valores das 
    # cotações diárias das açoes.
    # 
    # O comando bs4 abaixo, retorna todas as células com esses valores. 
    # Inspecione pelo browser o elemento para entender porque estou usando esse comando.  
    # Repare que a variável tags é uma lista de <td>
    
    # tags = soup.select('td.Py\(10px\)')

    # O comando abaixo navega pelo primeiro <td> retornado acima até encontrar seu conteúdo (o número que aparece na célula da tabela na página)
    #
    #tags[0].select('span')[0].string

    # Usando o comando acima com base, imprima o conteúdo de cada <td> retornado.  


    # 4.4 - O link abaixo permite fazer o download do mesmo conteúdo, usando os mesmos critérios acima. Use-o para baixar um arquivo para cada ação lida pelo programa

        # 'https://query1.finance.yahoo.com/v7/finance/download/VALE?period1=1577836800&period2=1609372800&interval=1d&events=history&includeAdjustedClose=true'


# OUTPUT: ao final:
# a) serão exibidos os valores diários de cada ação na tela.    
# b) haverá um arquivo para cada ação, com dados diários no período informado.
