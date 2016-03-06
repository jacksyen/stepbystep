package {{base_package}}.repository.{{sub_domain}};
package {{base_package}}.domain.{{sub_domain}}.{{domain_name}};

import org.springframework.data.jpa.repository.JpaRepository;

public interface {{domain_name}}Repository extends JpaRepository<{{domain_name}},Long> {

}