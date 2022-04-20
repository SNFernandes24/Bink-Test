from collections import defaultdict


def mastsOwnedPerTenant(reader):

    tenantOwned = defaultdict(int)

    # if tenant doesn't exist create new one else add one to value
    for row in reader:
        if tenantOwned[row["Tenant Name"]] is not None:
            if tenantOwned[row["Tenant Name"]] <= 0:
                tenantOwned[row["Tenant Name"]] = 1
            else:
                tenantOwned[row["Tenant Name"]] += 1

    # Format all tenants with masts owned
    finalTenantList = []
    for key, val in tenantOwned.items():
        if val <= 1:
            finalTenantList.append("Tenant {k} owns {v} mast.\n"
                                   .format(k=key, v=val))
        else:
            finalTenantList.append("Tenant {k} owns {v} masts.\n"
                                   .format(k=key, v=val))
    return "\n".join([str(x) for x in finalTenantList])
