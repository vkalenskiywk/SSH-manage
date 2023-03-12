def get_claims():
    import os
    database_f = os.listdir(path=r'D:\!Work\SSH\Database\claim')
    claims = [claim for claim in database_f if (len(claim) == 17) & (claim[13:] == ".SSH")]
    return claims
    # for a in database_f:
    #     print(len(a))
    #     print(a[12:])
    # print(claims)