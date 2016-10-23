<?php

namespace AppBundle\Repository;

use Doctrine\ORM\EntityRepository;

class LocationRepository extends EntityRepository
{

    public function filter($request)
    {
        // {{{

        $qb = $this->getEntityManager()->createQueryBuilder();

        $qb->select('l')
            ->from('AppBundle:Location', 'l')
            ->where('l.deletedAt is null')
            ->orderBy('l.id', 'ASC')
            ;

        if ($request->query->get('province')) {
            $qb->andWhere('l.province = :province');
            $qb->setParameter('province', $request->query->get('province'));
        }

        return $qb->getQuery()->getResult();

        // }}}
    }

}
