def patch_object(entity, attributes):
    '''A utility for updating objects with a PATCH method. '''
    for key, value in attributes.items():
        if isinstance(value, dict):
            sub_entity = getattr(entity, key)
            if isinstance(sub_entity, dict):
                _merge_dict_into(value, sub_entity)
                setattr(entity, key, sub_entity)
            else:
                patch_object(sub_entity, value)
        else:
            setattr(entity, key, value)


def _merge_dict_into(merge, into):
    '''values in `merge` replace those in `into`'''
    for key, value in merge.items():
        into[key] = value
