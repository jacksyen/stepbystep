package {{base_package}}.service;

import org.springframework.stereotype.Service;
import {{base_package}}.repository.{{sub_domain}}.{{domain_name}}Repository;
import org.springframework.transaction.annotation.EnableTransactionManagement;


@Service
@EnableTransactionManagement
public class {{domain_name}}Service {

    @Autowired
    private {{domain_name}}Repository {{domain_name}}Repository;

    public ServerInfo save({{domain_name}} instance){
        return this.{{domain_name}}Repository.save(info);
    }

    public void delete({{domain_name}} instance){
         this.{{domain_name}}Repository.delete(info);
    }

}