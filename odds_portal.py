#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:12:41 2019

@author: miketondu
"""

{  
   "_id":"oddsportal",
   "startUrl":[  
      "https://www.oddsportal.com/soccer/bolivia/division-profesional/results/"
   ],
   "selectors":[  
      {  
         "id":"match",
         "type":"SelectorLink",
         "parentSelectors":[  
            "_root"
         ],
         "selector":"td.name a",
         "multiple":true,
         "delay":0
      },
      {  
         "id":"odds",
         "type":"SelectorTable",
         "parentSelectors":[  
            "match"
         ],
         "selector":"div.table-container:nth-of-type(1) table.table-main",
         "multiple":true,
         "columns":[  
            {  
               "header":"Bookmakers",
               "name":"Bookmakers",
               "extract":true
            },
            {  
               "header":"1",
               "name":"Home Odds",
               "extract":true
            },
            {  
               "header":"X",
               "name":"Draw Odds",
               "extract":true
            },
            {  
               "header":"2",
               "name":"Away Odds",
               "extract":true
            },
            {  
               "header":"Payout",
               "name":"Payout",
               "extract":true
            }
         ],
         "delay":0,
         "tableDataRowSelector":"tbody tr",
         "tableHeaderRowSelector":"thead tr"
      },
         {"id":"results",
          "type":"SelectorText",
          "parentSelectors":[
                  "match"
                  ],
          "selector":"p.result",
          "multiple":false,
          "delay":0
          
                 },
         
      {  
         "id":"date",
         "type":"SelectorText",
         "parentSelectors":[  
            "match"
         ],
         "selector":"p.date",
         "multiple":false,
         "regex":"(?<=\\,)(.*?)(?=,)",
         "delay":0
      },
      {  
         "id":"time",
         "type":"SelectorText",
         "parentSelectors":[  
            "match"
         ],
         "selector":"p.date",
         "multiple":false,
         "regex":".{5}$",
         "delay":0
      }
   ]
}