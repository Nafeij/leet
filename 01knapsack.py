def knapsack(itms,W):
    dp = [0]*(W+1)

    for itm in itms:
        for w in range(W,0,-1):
            if itm['weight'] <= w:
                dp[w] = max(dp[w], dp[w-itm['weight']] + itm['value'])
    return dp[W]

if __name__ == '__main__':
    tests = [[[[{ 'name':'map', 'weight':9, 'value':150 }, { 'name':'compass', 'weight':13, 'value':35 },
                { 'name':'water', 'weight':153, 'value':200 }, { 'name':'sandwich', 'weight':50, 'value':160 },
                { 'name':'glucose', 'weight':15, 'value':60 }, { 'name':'tin', 'weight':68, 'value':45 },
                { 'name':'banana', 'weight':27, 'value':60 }, { 'name':'apple', 'weight':39, 'value':40 }], 100],405],
            [[[{ 'name':'map', 'weight':9, 'value':150 }, { 'name':'compass', 'weight':13, 'value':35 },
               { 'name':'water', 'weight':153, 'value':200 }, { 'name':'sandwich', 'weight':50, 'value':160 },
               { 'name':'glucose', 'weight':15, 'value':60 }, { 'name':'tin', 'weight':68, 'value':45 },
               { 'name':'banana', 'weight':27, 'value':60 }, { 'name':'apple', 'weight':39, 'value':40 }], 200],510],
            [[[{ 'name':'cheese', 'weight':23, 'value':30 }, { 'name':'beer', 'weight':52, 'value':10 },
               { 'name':'suntan cream', 'weight':11, 'value':70 }, { 'name':'camera', 'weight':32, 'value':30 },
               { 'name':'T-shirt', 'weight':24, 'value':15 }, { 'name':'trousers', 'weight':48, 'value':10 },
               { 'name':'umbrella', 'weight':73, 'value':40 }], 100],145],
            [[[{ 'name':'cheese', 'weight':23, 'value':30 }, { 'name':'beer', 'weight':52, 'value':10 },
               { 'name':'suntan cream', 'weight':11, 'value':70 }, { 'name':'camera', 'weight':32, 'value':30 },
               { 'name':'T-shirt', 'weight':24, 'value':15 }, { 'name':'trousers', 'weight':48, 'value':10 },
               { 'name':'umbrella', 'weight':73, 'value':40 }], 200],185],
            [[[{ 'name':'waterproof trousers', 'weight':42, 'value':70 },
               { 'name':'waterproof overclothes', 'weight':43, 'value':75 },
               { 'name':'note-case', 'weight':22, 'value':80 }, { 'name':'sunglasses', 'weight':7, 'value':20 }, 
               { 'name':'towel', 'weight':18, 'value':12 }, { 'name':'socks', 'weight':4, 'value':50 },
               { 'name':'book', 'weight':30, 'value':10 }], 100],237],
            [[[{ 'name':'waterproof trousers', 'weight':42, 'value':70 },
               { 'name':'waterproof overclothes', 'weight':43, 'value':75 },
               { 'name':'note-case', 'weight':22, 'value':80 }, { 'name':'sunglasses', 'weight':7, 'value':20 },
               { 'name':'towel', 'weight':18, 'value':12 }, { 'name':'socks', 'weight':4, 'value':50 },
               { 'name':'book', 'weight':30, 'value':10 }], 200],317]]

    for t in tests:
        assert knapsack(t[0][0],t[0][1]) == t[1]

