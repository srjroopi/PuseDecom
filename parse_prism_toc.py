def parse_prism_toc(Toc_response_data):
    if Toc_response_data.get("productId") and len(Toc_response_data.get("children", [])) > 1:
        print("--------------------")
        return ('passed parse')
    else:
        print("not passed")