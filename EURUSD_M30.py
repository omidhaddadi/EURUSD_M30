//+------------------------------------------------------------------+
//|                                                   EURUSD_M30_v01 |
//|                                     Copyright 2023, Omid Haddadi |
//|                                                                  |
//+------------------------------------------------------------------+

int start()
  {
   double lot_buy_01=0.01,lot_sell_01=0.01,lot_buy_02=0.01,lot_sell_02=0.01;
   double stoploss=0.01;
   double takeprofit=0.011;
   double stoploss2=(5000*Point);
   double takeprofit2=(7000*Point);
   int DXPeriod=200, DXPeriod2=300,DXPeriod3=140,j=0;
   int wait_minute=5;
   int starti,i=DXPeriod,counted_bars=IndicatorCounted();
   int q,p,m,n,total_order=OrdersTotal();
   double acc_equity=AccountEquity();



   int startHour = 1;     // 1 AM
   int startMinute = 29; // 29 minutes
   int endHour = 23;     // 11 PM
   int endMinute = 59;   // 59 minutes
   
   // Get the current server time
    datetime serverTime = TimeCurrent();
    // Extract the hour and minute from the server time
    int currentHour = Hour();
    int currentMinute = Minute();
    // Calculate the current time in minutes since midnight
    int currentTimeInMinutes = currentHour * 60 + currentMinute;
    // Calculate the start time and end time in minutes since midnight
    int startTimeInMinutes = startHour * 60 + startMinute;
    int endTimeInMinutes = endHour * 60 + endMinute;
    
    
    // Check if the current time is within the allowed trading hours
    if (((currentTimeInMinutes > startTimeInMinutes && currentTimeInMinutes < endTimeInMinutes))&&((currentMinute<1) || (currentMinute>59)||(currentMinute>29 && currentMinute<31)))
      {




      for(int k=total_order-1; k>=0; k--)
         {
                if (OrderSelect(k, SELECT_BY_POS)){
                     if(OrderType()==OP_BUY && OrderSymbol()=="EURUSD"){q=1;}
                     if(OrderType()==OP_SELL && OrderSymbol()=="EURUSD"){p=1;}
               }
         }




      double DXPeriod11=18;
      double atr1=iATR(Symbol(),0,DXPeriod11,0);
      double atr_30M1=iATR(Symbol(),PERIOD_M30,112,0);            
      double adx1=iADX(Symbol(),0,DXPeriod11,PRICE_CLOSE,0,0);
      double bestbuy1=iADX(Symbol(),0,DXPeriod11,PRICE_CLOSE,1,0);
      double bestsell1=iADX(Symbol(),0,DXPeriod11,PRICE_CLOSE,2,0);
      double sar_value1=iSAR(NULL,0,0.02,0.2,0);
      double bb_up_value1=iBands(NULL,0,30,0.5,0,PRICE_HIGH,MODE_UPPER,3);
      double bb_low_value1=iBands(NULL,0,30,0.5,0,PRICE_LOW,MODE_LOWER,3);
      double envel_up_value1=iEnvelopes(NULL,0,40,MODE_SMA,0,PRICE_HIGH,0.38,MODE_UPPER,2);
      double envel_low_value1=iEnvelopes(NULL,0,40,MODE_SMA,0,PRICE_LOW,0.38,MODE_LOWER,2);
      double max_bb_envel1= MathMax(bb_up_value1,envel_up_value1);
      double min_bb_envel1= MathMin(bb_low_value1,envel_low_value1);
      double rsi1 = iRSI(NULL,PERIOD_M30,112,PRICE_CLOSE,0);
      double ma1=iMA(NULL,PERIOD_D1,5,0,MODE_SMA,PRICE_CLOSE,0);
      double atr_30M11=iATR(Symbol(),PERIOD_M30,5,0);
      double wpr1=-1*(iWPR(Symbol(),PERIOD_D1,112,0));
           

      if((q==0)&&(bestsell1>2)&&(adx1<20)&&(bestbuy1<150)&&(Bid<min_bb_envel1)&&(atr_30M1<(Bid*3.5/800))&&(1<Bid/atr_30M11)&&(1000>Bid/atr_30M11)&&(Bid>ma1)&&(rsi1>50)&&(wpr1>80)){n=0;      
         OrderSend(Symbol(),OP_BUY,0.0000013*(acc_equity/(Bid*takeprofit)),Bid,10,Bid-(Bid*stoploss),Bid+(Bid*takeprofit),"EURUSD_M30_v01_1");
}
      if((q==0)&&(bestsell1>10)&&(adx1>30)&&(bestbuy1<25)&&(Bid>max_bb_envel1)&&(atr_30M1>(Bid*1.5/800))&&(400<Bid/atr_30M11)&&(500>Bid/atr_30M11)&&(Bid>ma1)&&(rsi1>55)&&(wpr1>60)){n=0;      
         OrderSend(Symbol(),OP_BUY,0.0000013*(acc_equity/(Bid*takeprofit)),Bid,10,Bid-(Bid*stoploss),Bid+(Bid*takeprofit),"EURUSD_M30_v01_1");
}
      if((p==0)&&(bestsell1>15)&&(adx1>40)&&(bestbuy1>5)&&(Bid<min_bb_envel1)&&(atr_30M1<(Bid*1.5/800))&&(1000<Bid/atr_30M11)&&(10000>Bid/atr_30M11)&&(Bid>ma1)&&(rsi1>50)&&(wpr1<70)){n=0;      
         OrderSend(Symbol(),OP_SELL,0.0000013*(acc_equity/(Bid*takeprofit)),Bid,10,Bid+(Bid*stoploss),Bid-(Bid*takeprofit),"EURUSD_M30_v01_1");
}
      if((p==0)&&(bestsell1>-4)&&(adx1>50)&&(bestbuy1>-27)&&(Bid>max_bb_envel1)&&(atr_30M1<(Bid*1/800))&&(1000<Bid/atr_30M11)&&(10000>Bid/atr_30M11)&&(Bid>ma1)&&(rsi1>52)&&(rsi1<55)&&(wpr1<25)){n=0;      
         OrderSend(Symbol(),OP_SELL,0.0000013*(acc_equity/(Bid*takeprofit)),Bid,10,Bid+(Bid*stoploss),Bid-(Bid*takeprofit),"EURUSD_M30_v01_1");
}



}
   return(0);

  }
//+------------------------------------------------------------------+