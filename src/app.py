import praw

palavras_para_proibir = ['palavra1', 'palavra2', 'palavra3']

#função criada para organizar
def liner():
    print('--------------------------------------')

reddit = praw.Reddit(client_id="ajdTuMcPDDDg9g",

                     client_secret="mhjOAAAz8u4tTq50JUp1bGnj3NQ",
                     username='coloque_seu_username_aqui',
                     password='coloque_sua_senha_aqui',
                     user_agent="my user agent")

sub_selected = reddit.subreddit("escolha_o_subreddit")

liner()
print(sub_selected.title)
print(sub_selected.description)
liner()

# retorna as 2 peirmeiras top postagens do subreddit
for submission in sub_selected.top(limit=2):
    redditor = submission.author
    auth = redditor.name
    title = submission.title
    i_d = submission.id

    print(f'Autor: {auth}')
    print(f'Título: {title}')
    print(f'id: {i_d}')
    liner()

    liner()
    print('Comentarios:')
    liner()

    # comentarios por id
    post = reddit.submission(id=i_d)
    for top_level_comment in post.comments:

        comentario = top_level_comment.body
        comentarista = top_level_comment.author
        nome_do_comentarista = comentarista.name

        # mais um for para procurar a palavra para bloquear
        for palavra in palavras_para_proibir:
            comentario = comentario.replace(palavra, "*****")

        liner()
        print(f'Nome: {nome_do_comentarista}')
        print(f'Comentário: {comentario}')
