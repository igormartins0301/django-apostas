def feature_engineering(df):
    lista_resultado = ['Odd_H', 'Odd_D', 'Odd_A']
    lista_under_e_over = ['Odd_Over25', 'Odd_Under25']

    for coluna_resultado in lista_resultado:
        for coluna_under_over in lista_under_e_over:
            nova_coluna_nome = f"{coluna_resultado}_{coluna_under_over}"
            df[nova_coluna_nome] = df[coluna_resultado] / df[coluna_under_over]
            df['Diff_HA'] = df['Odd_H'] - df['Odd_A']
            df['Odd_Over25_Odd_Under25'] = df['Odd_Over25'] / df['Odd_Under25']
            df['Diff_HD'] = df['Odd_H'] - df['Odd_D']
            df['Diff_DA'] = df['Odd_D'] - df['Odd_A']
            df['Diff_OU'] = df['Odd_Over25'] - df['Odd_Under25']
            df['Avg_H'] = df[['Odd_H', 'Odd_D', 'Odd_A']].mean(axis=1)
            df['Max_H'] = df[['Odd_H', 'Odd_D', 'Odd_A']].max(axis=1)
            df['Ratio_HA'] = df['Odd_H'] / df['Odd_A']
            df['Ratio_HD'] = df['Odd_H'] / df['Odd_D']
            df['Ratio_DA'] = df['Odd_D'] / df['Odd_A']
            df['Prob_H'] = 1 / df['Odd_H']
            df['Prob_D'] = 1 / df['Odd_D']
            df['Prob_A'] = 1 / df['Odd_A']
            df['Log_Odd_H'] = -1 * df['Odd_H'].apply(lambda x: 0 if x == 0 else (1 / x))
            df['diff_X_over25'] = df['Diff_HA'] * df['Odd_Over25']
            df['diff_X_under25'] = df['Diff_HA'] * df['Odd_Under25']
            df['odds_diff'] = df['Odd_H'] - df['Odd_A']
            df['total_gols_previstos'] = df['Odd_Under25'] + df['Odd_Over25']
            df['intersecao_mandante_under'] = df['Odd_H'] * df['Odd_Under25']
            df['intersecao_mandante_over'] = df['Odd_H'] * df['Odd_Over25']
            df['intersecao_visitante_under'] = df['Odd_A'] * df['Odd_Under25']
            df['intersecao_visitante_over'] = df['Odd_A'] * df['Odd_Over25']

    df = df.dropna()

    return df