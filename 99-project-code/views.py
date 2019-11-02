import random
from django.views.generic import View

from django.http import JsonResponse
# from django.http import HttpResponse
from django.template.response import TemplateResponse
from mysite.models import (
    BingoCard,
    BuyCard,
    PlayerAccount,
    BallCall,
    BingoGame,
    Pattern
)

class BingoCardView(View):
    def get(self, request, **kwargs):
        seed = kwargs.get('c') or random.randrange(1, 100000)
        card = BingoCard(seed)
        context = {'values': card.values}
        return TemplateResponse(request, 'bingocard.html', context)
        return JsonResponse(card.to_json())



class BuyCardView(View):
    def get(self, request, **kwargs):
        account = PlayerAccount.objects.filter(id=kwargs.get('a')).first()
        card_id = kwargs.get('b')
        value = kwargs.get('v')
        buycard = BuyCard.objects.create(account=account, card_id=card_id, cost=value)
        account.credits-=value
        account.save()
        ballcall_id = random.randrange(1, 100000)
        game = BingoGame.objects.create(buy_card=buycard, ball_call=ballcall_id)
        all_patterns = Pattern.objects.all()
        bingocard = BingoCard(card_id)
        ballcall = BallCall(ballcall_id)
        totalwin = 0
        for pattern in all_patterns:
            required = bingocard.pattern_values(pattern)
            for x in required:
                if x in ballcall.balls[0:pattern.ballcount]:
                    totalwin+=pattern.prize
        return JsonResponse({
            'game_id': game.id,
            'buycard_id': buycard.id,
            'total_win': totalwin
            })


class PlayGameView(View):
    def get(self, request, **kwargs):
        # account = PlayerAccount.objects.all()
        # card_id = BuyCard.card_id
        # credits = PlayerAccount.credits
        context = {'accounts': PlayerAccount.objects.all()
        }
        return TemplateResponse(request, 'buy_card_form.html', context)

    def post(self, request, *args, **kwargs):
        return JsonResponse(request.POST)


class GameResultView(View):
    def post(self, request, *args, **kwargs):
        account = PlayerAccount.objects.filter(id=request.POST.get('account')).first()
        card_id = int(request.POST.get('bingo_card_id'))
        value = int(request.POST.get('credits'))
        buycard = BuyCard.objects.create(account=account, card_id=card_id, cost=value)
        account.credits-=value
        account.save()
        ballcall_id = random.randrange(1, 100000)
        game = BingoGame.objects.create(buy_card=buycard, ball_call=ballcall_id)
        all_patterns = Pattern.objects.all()
        bingocard = BingoCard(card_id)
        ballcall = BallCall(ballcall_id)
        totalwin = 0
        patterns_won = []
        hits = [0]
        for pattern in all_patterns:
            required = bingocard.pattern_values(pattern)
            all_hit = True
            for x in required:
                if x not in ballcall.balls[0:pattern.ball_count]:
                    all_hit = False
                    break
            if all_hit:
                totalwin+=pattern.prize
                patterns_won.append(pattern.name)
                hits.extend(required)
        account.credits+=totalwin
        account.save()

        # Turning hits into a list, the easy to read way
        # str_hits = []
        # for hit in hits
        #     str_hits.append(f'.a{hit}])
        # ', '.join(str_hits)

        # Turning hits int o a list, with a comprehension
        # hits_str = ', '.join([f'.a{hit}' for hit in hits])

        context = {
            'values' : bingocard.values,
            'account': account,
            'bingocard': bingocard,
            'ballcall': ballcall,
            'patterns_won': patterns_won,
            'total_win': totalwin,
            'hits': ', '.join([f'.a{hit}' for hit in hits]),
        }
        return TemplateResponse(request, 'show_result.html', context)



class BallCallView(View):
    def get(self, request, **kwargs):
        seed = kwargs.get('bc') or random.randrange(1, 100000)
        ball_call = BallCall(seed)
        return JsonResponse(ball_call.to_json())
