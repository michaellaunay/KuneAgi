# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# avalaible on http://www.gnu.org/licenses/agpl.html 

# licence: AGPL
# author: Amen Souissi


def get_folder_content(folder, user,
                       add_query=None,
                       sort_on='release_date', reverse=True,
                       **args):
    return folder.contents
