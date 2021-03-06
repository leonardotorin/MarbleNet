import numpy as np
import random

'''
Estrategia de Epsilon Greedy vai ser usada como um trade off entre exploracao e tirar vantagem de
algo ja conhecido como efetivo.
Isso impede de o modelo achar uma estrategia viavel (mas que nao da tanta recompensa como 
alguma estrategia um pouco mais distante) e repetir ela infinitamente.
Comecamos com uma probabilidade alta de exploracao (porque a rede neural nao sabe o que eh
bom ainda), e eh inserido um decaimento exponencial nessa probabilidade, para cada vez mais
o agente depender do modelo, que ja vai estar mais robusto.


Argumentos:

sess: Sessao do tensorflow
prob_inicial: probabilidade de exploracao no comeco
min_prob: probabilidade minima de exploracao (nao cai mais que isso no decaimento exponencial)
tx_decay: taxa do decaimento exponencial (lambda da distruibicao exponencial)
passo_decay: qual passo esta do decaimento
estado: imagem do estado que esta no jogo
acoes_possiveis: acoes possiveis (em vetor de vetores) 
'''

def eg(env, sess, prob_inicial, min_prob, tx_decay, passo_decay, estado_emp):
	#define um numero aleatorio como o tradeoff entre exploracao e tirar vantagem
	exp_vant_tradeoff = np.random.rand()

	#probabilidade de exploracao
	prob_exp = min_prob + (prob_inicial - min_prob) * np.exp(-tx_decay * passo_decay)

	if (prob_exp > exp_vant_tradeoff):
		print('Explorando')
		#explora
		acao = env.action_space.sample()

	else:
		print('Abusando')
		#procura melhor acao baseada na estimacao do Q-valor da rede neural
		Qs = sess.run(DQRede.saida, feed_dict = {
													DQRede.inputs: estado_emp.reshape((1, *estado_emp.shape))
												}
					)

		#procura o indice da melhor acao
		#acao = acoes_possiveis[np.argmax(Qs)]
		acao = np.argmax(Qs)

	return acao, prob_exp