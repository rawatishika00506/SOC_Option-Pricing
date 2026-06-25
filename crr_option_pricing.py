import numpy as np

def crr_put_price(S0,K,T,r,sigma,steps,american=True):
    dt=T/steps
    u=np.exp(sigma*np.sqrt(dt))
    d=1/u
    p=(np.exp(r*dt)-d)/(u-d)
    disc=np.exp(-r*dt)

    stock=np.array([S0*(u**j)*(d**(steps-j)) for j in range(steps+1)])
    option=np.maximum(K-stock,0)

    for i in range(steps-1,-1,-1):
        new=[]
        for j in range(i+1):
            cont=disc*(p*option[j+1]+(1-p)*option[j])
            if american:
                s=S0*(u**j)*(d**(i-j))
                ex=max(K-s,0)
                new.append(max(cont,ex))
            else:
                new.append(cont)
        option=np.array(new)
    return option[0]

if __name__=="__main__":
    euro=crr_put_price(100,100,1,0.05,0.25,500,False)
    amer=crr_put_price(100,100,1,0.05,0.25,500,True)
    print("European Put:",round(euro,4))
    print("American Put :",round(amer,4))
    print("Early Exercise Premium:",round(amer-euro,4))
