<?php

namespace AppBundle\Repository;

use Doctrine\ORM\EntityRepository;

class ProvinceRepository extends EntityRepository
{

    public function filter($request)
    {
        // {{{

        $qb = $this->getEntityManager()->createQueryBuilder();

        $qb->select('p')
            ->from('AppBundle:Province', 'p')
            ->where('p.deletedAt is null')
            ->orderBy('p.id', 'ASC')
            ;

        return $qb->getQuery()->getResult();

        // }}}
    }

}
