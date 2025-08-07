-- criando tablespace para o Projeto BD ERP multi empresa
create tablespace er_mult_tst
    datafile
    'C:\Users\lucas\OneDrive\Documentos\GitHub\MINI_ERP_MULTIEMPRESAS\DDL\erp_mult_test.dbf'
    size 100m autoextend on next 50m maxsize 500m
    online
    permanent
    extent management local autoallocate
    segment space management auto;
    
-- criando usuario

create user user_test
    identified by 123456
    default tablespace er_mult_tst
    temporary tablespace TEMP;
    
-- concedendo permissões para o usuario
grant ALL PRIVILEGES to user_test;

-- alterando limite de cota para usuario
alter user user_test quota unlimited on er_mult_tst;


-- criando o tablespace para o projeto BD erp mult empresa PRODUCAO
create tablespace erp_mult_prd
    datafile
    'C:\Users\lucas\OneDrive\Documentos\GitHub\MINI_ERP_MULTIEMPRESAS\DDL\erp_mult_prd.dbf'
    size 100m autoextend on next 50m maxsize 500m
    online
    extent management local autoallocate
    segment space management auto;
    
-- criando usario producao
create user user_prd
    identified by 123456
    default tablespace erp_mult_prd
    temporary tablespace temp;
    
-- garantindo privilegios ao usuario
grant all privileges to user_prd;

-- alterando limite de cota para o usuario de producao
alter user user_prd quota unlimited on erp_mult_prd;

-- drop objetos
/*
drop user user_prd CASCADE;
drop user user_test CASCADE;

drop tablespace erp_mult_prd INCLUDING CONTENTS AND DATAFILES;
drop tablespace er_mult_tst INCLUDING CONTENTS AND DATAFILES;
*/