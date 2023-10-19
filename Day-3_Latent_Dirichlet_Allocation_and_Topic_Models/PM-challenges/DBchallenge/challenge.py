#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dbConnect import singleQuery
#import gensim


# query para traer 10 noticias
noticias = singleQuery('SELECT titulo,cuerpo,fuente FROM noticias LIMIT 10;')